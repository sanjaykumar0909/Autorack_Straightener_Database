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

try{
    $c_start_time = Get-Date $start_time
    $c_end_time = Get-Date $end_time
}catch{
    Write-Host "invalid date format"
    exit 1
}
# Write-Host $c_start_time $c_start_time.gettype()
# Write-Host $c_end_time $c_end_time.GetType()

$isSuccess = [int]::TryParse($fetch_choice, [ref]$fetch_choice)
if (-not $isSuccess) {
    Write-Host "Invalid fetch_choice value. Please enter 1, 2, or 3."
    exit 1
}

$file_list = Get-ChildItem -Path $folder_path

$files = @()
switch ($fetch_choice) {
    1{ 
        $files = $file_list | Where-Object {
            ($_.LastWriteTime -gt $c_start_time) -and ($_.LastWriteTime -lt $c_end_time)
        }
    }
    2{
        $files = $file_list | Where-Object {
            ($_.CreationTime -gt $c_start_time) -and ($_.CreationTime -lt $c_end_time)
        }
    }
    3{
        $files = $file_list | Where-Object {
            ($_.LastAccessTime -gt $c_start_time) -and ($_.LastAccessTime -lt $c_end_time)
        }
    }
    Default {
        Write-Host "Invalid fetch_choice value. Please enter 1, 2, or 3."
        exit 1
    }
}
$files | ForEach-Object { Write-Host $_.Name }