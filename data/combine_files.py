import glob

def combine_files():
    """
    use this to combine all files in a folder with the same ext

    the terminal commands could also be used.
    head -1 director/one_file.csv > output csv   ## writing the header to the final file
    tail -n +2  director/*.csv >> output.csv  ## w
    """
    # ask user for combine file extension
    combine_extension = input('which files are you combining? (ex: csv, txt, etc.): ').lower()
    
    #ask user for name of new file
    new_file_name = input('what would you like the output file name to be? (the extension requested previously will be used as the output file extension): ')

    # gather all of the files with designated extension
    all_files = glob.glob(f'*.{combine_extension}') 
    
    # header boolean    
    keep_header = False

    # open new file named output in write binary mode
    with open(f'{new_file_name}.{combine_extension}','w') as new_file:
    
        # loop through all files and write to output file
        for file_name in all_files:
            
            print(f'adding "{file_name}" data to {new_file_name}')
            with open(file_name) as fin:
                
                # get header of file
                header = next(fin)
                
                # change header boolean so if statement will execute
                if not keep_header:

                    # write header to new file
                    new_file.write(header)
                    
                    # change header boolean to True so if statment will not execute again
                    keep_header = True

                # write remaining lines to new file
                for line in fin:
                    new_file.write(line)
                    
# call combine_files function
combine_files()