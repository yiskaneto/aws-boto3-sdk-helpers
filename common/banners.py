def cleanup_start_msg(resource_name):
    """
    Clean-up message for cloud resources
    """
    msg = f"""\n
################################################
#
#    Clean-up started for {resource_name}
#
###############################################
\n"""

    return print(msg)
