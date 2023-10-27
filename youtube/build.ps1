$exclude = @("venv", "youtube.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "youtube.zip" -Force