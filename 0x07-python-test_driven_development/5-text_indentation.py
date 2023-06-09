#!/usr/bin/python3

"""
This module defines a function to print a text with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of ., ? and :

    Args:
        text (str): The input text

    Raises:
        TypeError: If text is not a string

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    separators = (".", "?", ":")
    result = ""
    
    for char in text:
        result += char
        if char in separators:
            result += "\n\n"
    
    print(result.strip())

if __name__ == "__main__":
    text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres")
