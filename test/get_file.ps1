param(
    [string]$months_elapsed_str,
    [string]$ser_num_count_str
)
[int]$months_elapsed = $months_elapsed_str
[int]$ser_num_count = $ser_num_count_str
# Write-Host $months_elapsed.GetType() $ser_num_count.GetType()
$FOLDER_PATH = "C:\Users\2003s\OneDrive\Desktop\Internship\csv_fold"
function Get-SortedFilesByMonth {
    param (
        [int]$Month,
        [int]$Year
    )
    $FolderPath = $FOLDER_PATH
    # Retrieve and sort files by CreationTime
    $sortedFiles = Get-ChildItem -Path $FolderPath -File |
                   Where-Object { $_.CreationTime.Month -eq $Month -and $_.CreationTime.Year -eq $Year } |
                   Sort-Object CreationTime

    return $sortedFiles
}
function Add-MonthsToDate {
    param (
        [DateTime]$date,
        [int]$months_to_add
    )
    
    return $date.AddMonths($months_to_add)
}

# change chrono
$START_CHRONO = Get-Date "1/8/2023"

$file_in_time = Add-MonthsToDate -date $START_CHRONO -months_to_add ($months_elapsed-1)
# Write-Host $file_in_time
$file_list = Get-SortedFilesByMonth -Month $file_in_time.Month -Year $file_in_time.Year
# Write-Host $file_list

if($file_list.Length -eq 0){
    Write-Host -1
}elseif ($ser_num_count -gt $file_list.Length){
    Write-Host -2
}else{
    Write-Host $file_list[$ser_num_count-1].Name
}
