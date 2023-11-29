param(
    [string]$folder_path,
    [string]$fetch_choice,
    [string]$start_time,
    [string]$end_time
)

# Validate the folder path
if (-not (Test-Path $folder_path)) {
    Write-Host "Invalid directory path."
    exit 1
}

# Parse the date strings
try {
    $start_time = Get-Date -Date $start_time -Format "dd/MM/yyyy HH:mm:ss"
    $start_time = Get-Date $start_time
    $end_time = Get-Date -Date $end_time -Format "dd/MM/yyyy HH:mm:ss"
    $end_time = Get-Date $end_time
} catch {
    Write-Host "Invalid date format."
    exit 1
}

# Parse fetch_choice
$isSuccess = [int]::TryParse($fetch_choice, [ref]$fetch_choice)
if (-not $isSuccess) {
    Write-Host "Invalid fetch_choice value. Please enter 1, 2, or 3."
    exit 1
}

# Get the list of files in the folder
$file_list = Get-ChildItem -Path $folder_path

# Fetch files based on the criteria specified by fetch_choice
$files = @()
switch ($fetch_choice) {
    1 {
        $files = $file_list | Where-Object {
            (Get-Date $_.LastWriteTime -Format "dd/MM/yyyy HH:mm:ss") -ge $start_time -and (Get-Date $_.LastWriteTime -Format "dd/MM/yyyy HH:mm:ss") -le $end_time
        }
    }
    2 {
        $files = $file_list | Where-Object {
            (Get-Date $_.CreationTime -Format "dd/MM/yyyy HH:mm:ss") -ge $start_time -and (Get-Date $_.CreationTime -Format "dd/MM/yyyy HH:mm:ss") -le $end_time
        }
    }
    3 {
        $files = $file_list | Where-Object {
            (Get-Date $_.LastAccessTime -Format "dd/MM/yyyy HH:mm:ss") -ge $start_time -and (Get-Date $_.LastAccessTime -Format "dd/MM/yyyy HH:mm:ss") -le $end_time
        }
    }
    Default {
        Write-Host "Invalid fetch_choice value. Please enter 1, 2, or 3."
        exit 1
    }
}

# Display the list of files
if ($files.Count -eq 0) {
    Write-Host "No files match the given criteria."
} else {
    Write-Host "Files matching the criteria:"
    $files | ForEach-Object { Write-Host $_.Name }
}
