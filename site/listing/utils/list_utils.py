from typing import List, Any


def divide_into_sublist(listing: List[Any], div_by: int) -> List[List[Any]]:
    """
    Takes a list and divides it into sublists, where each sublists has a maximum of items as the div_by passed value.
    """

    # Special case when the length of the list is less than or equal to the sublist amount
    if len(listing) <= div_by:
        return [listing]

    result = list()
    for listing_stop in range(div_by, len(listing), div_by):
        result.append(listing[listing_stop - div_by:listing_stop:])

    return result
