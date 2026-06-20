$projectDir = $PWD


Write-Host "Installing Dependencies..." -ForegroundColor Green
python -m venv venv
.\venv\Scripts\pip install -r requirements.txt

# create profile if doesn't exist
if (!(Test-Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}

# remove old empo if exists
if (Get-Content $PROFILE) {
    (Get-Content $PROFILE) | Where-Object { $_ -notmatch "function empo" } | Set-Content $PROFILE
}

# add empo function
Add-Content $PROFILE "function empo { & `"$projectDir\venv\Scripts\python`" `"$projectDir\main.py`" @args }"

Write-Host "Successfully installed empo!" -ForegroundColor Green
Write-Host "Restart your terminal and run 'empo' to get started!" -ForegroundColor Yellow
exit
