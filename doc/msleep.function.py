
msleep_function = {
    "name": "msleep",
    "topic": "deadline",
    "info": "waits until deadline expires",
    "args": [],
    "result": {
        "type": "int",
        "success": "0",
        "error": "-1",
    },

    "has_deadline": True,

    "prologue": """
        This function blocks until the deadline expires or an error occurs.
        In the former case it returns zero.
    """,

    "example": """
        int rc = msleep(now() + 1000);
        if(rc != 0) {
            perror("Cannot sleep");
            exit(1);
        }
        printf("Slept succefully for 1 second.\\n");
    """,
}

new_function(msleep_function)

