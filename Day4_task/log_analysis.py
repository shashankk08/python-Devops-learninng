try:
    f= open("app.log","r")
    
    info=0
    error=0
    warning=0

    for line in f:    
        if "INFO" in line:
            info=info+1
        elif "WARNING" in line:
            warning=warning+1
        elif "ERROR" in line:
            error=error+1        



except Exception as e:
    print("Error in system :",e)    


with open("log_summary.txt","w") as op_files:
    content=(f"INFO count is : {info} "
            f" WARNING count is : {warning} "
            f" ERROR count is : {error}")
    op_files.write(content)

    print(content)