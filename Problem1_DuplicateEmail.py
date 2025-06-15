import pandas as pd

#soln1 using drop_duplicates
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',inplace=True)
    person.drop_duplicates(subset='email',keep='first',inplace=True)

#soln 2: Using group by
    min_id=person.groupby('email')['id'].transform('min')
    id_to_delete=person[person['id']!=min_id]
    person.drop(id_to_delete.index,inplace=True)