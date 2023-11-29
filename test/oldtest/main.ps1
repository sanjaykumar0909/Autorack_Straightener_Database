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
Write-Host $start_time
Write-Host $end_time

# Parse the date strings
try {
    $c_start_time = [datetime]::ParseExact($start_time, "dd/MM/yyyy HH:mm:ss", [Globalization.CultureInfo]::InvariantCulture)
    $c_end_time = [datetime]::ParseExact($end_time, "dd/MM/yyyy HH:mm:ss", [Globalization.CultureInfo]::InvariantCulture)
} catch {
    Write-Host "Invalid date format."
    exit 1
}
Write-Host $c_start_time $c_start_time.GetType() 
write-host $c_end_time $c_end_time.GetType()

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
            (Get-Date $_.LastWriteTime -Format "dd/MM/yyyy HH:mm:ss") -ge $c_start_time -and (Get-Date $_.LastWriteTime -Format "dd/MM/yyyy HH:mm:ss") -le $c_end_time
        }
    }
    2 {
        $files = $file_list | Where-Object {
            (Get-Date $_.CreationTime -Format "dd/MM/yyyy HH:mm:ss") -ge $c_start_time -and (Get-Date $_.CreationTime -Format "dd/MM/yyyy HH:mm:ss") -le $c_end_time
        }
    }
    3 {
        $files = $file_list | Where-Object {
            (Get-Date $_.LastAccessTime -Format "dd/MM/yyyy HH:mm:ss") -ge $c_start_time -and (Get-Date $_.LastAccessTime -Format "dd/MM/yyyy HH:mm:ss") -le $c_end_time
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
