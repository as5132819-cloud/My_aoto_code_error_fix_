name: AI_Pull_Request_Fixer

on: [push]

permissions:
  contents: write
  pull-requests: write

jobs:
  debug-process:
    # Sirf tab chale jab user khud code push kare (AI ke PRs par na chale)
    if: github.actor != 'github-actions[bot]'
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Execute and Capture Error
        id: run_script
        continue-on-error: true
        run: |
          python3 code_with_error.py 2> log.txt

      - name: AI Fix and Create PR
        if: steps.run_script.outcome == 'failure'
        env:
          GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }} # Built-in token for PRs
        run: |
          pip install -q groq
          ERROR_MSG=$(cat log.txt)
          
          # 1. AI fixes the file locally
          python3 ai_debugger.py "$ERROR_MSG"
          
          # 2. Setup Git
          git config --global user.name "ai-bot"
          git config --global user.email "ai-bot@github.com"
          
          # 3. Create a new branch for the fix
          BRANCH_NAME="ai-fix-${{ github.run_id }}"
          git checkout -b $BRANCH_NAME
          
          # 4. Commit and Push the new branch
          git add code_with_error.py
          git commit -m "🤖 AI: Suggested fix for syntax error"
          git push origin $BRANCH_NAME
          
          # 5. Create the Pull Request using GitHub CLI
          gh pr create \
            --title "🤖 AI Fix: Corrected error in code_with_error.py" \
            --body "I found an error in your code. Here is the fix: \n\n \`\`\` \n $(cat log.txt) \n \`\`\`" \
            --base main \
            --head $BRANCH_NAME
