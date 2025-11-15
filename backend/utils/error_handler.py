def handle_errors(error):
    return {
        "error": str(error),
        "message": "Something went wrong"
    }, 500
