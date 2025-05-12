def hello(firstname="GitHub", lastname="Actions"):
    if not isinstance(firstname, str) or not isinstance(lastname, str):
        raise TypeError("Format de nom invalide. Veuillez entrer une chaîne de caractères.")

    # Si un seul argument est passé, on peut donc supposer que lastname n’est pas utilisé
    if lastname == "Actions" and firstname != "GitHub":
        return f"Hello, {firstname}!"
    
    return f"Hello, {firstname} {lastname}!"
