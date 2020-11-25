from app import db, DBTable

# set up your scraping below

rows = {
    "row1": "row1_val",
    "row2": "row2_val",
} 

# this `main` function should run your scraping when 
# this script is ran.
def main():
    db.drop_all()
    db.create_all()
    for key,val in rows.items():
        new_row = DBTable(column_1=key, column_2=val)
        print(new_row)
        db.session.add(new_row)
        db.session.commit()

if __name__ == '__main__':
    main()