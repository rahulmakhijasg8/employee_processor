import pandas as pd
from datetime import datetime, timedelta

def process_employee_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    
    print("Original DataFrame:")
    print(df)
    
    df['Date of Joining'] = pd.to_datetime(df['Date of Joining'])
    
    processed_df = df.copy()
    
    total_salary_by_dept = df.groupby('Department')['Salary'].sum()
    print("\n1. Total salary paid per department:")
    print(total_salary_by_dept)
    
    current_date = datetime.now()
    two_years_ago = current_date - timedelta(days=2*365)
    long_term_employees = df[df['Date of Joining'] < two_years_ago]
    print("\n2. Employees who have been with the company for more than 2 years:")
    print(long_term_employees[['Name', 'Department', 'Date of Joining']])
    
    top_paid_employees = df.sort_values(by='Salary', ascending=False)
    print("\n3. Top 3 highest-paid employees:")
    print(top_paid_employees[['Name', 'Department', 'Salary']][0:3])

    # the above thing can be done in one more way

    top_paid_employees = df.nlargest(3, 'Salary')
    print("\n3(V2). Top 3 highest-paid employees:")
    print(top_paid_employees[['Name', 'Department', 'Salary']])
    
    processed_df['Annual Salary'] = processed_df['Salary'] * 6
    print("\n4. DataFrame with Annual Salary column:")
    print(processed_df[['Name', 'Salary', 'Annual Salary']])
    
    avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
    print("\n5. Average salary per department:")
    print(avg_salary_by_dept)
    
    return processed_df

if __name__ == "__main__":
    file_path = 'sample_data.csv'
    
    try:
        result_df = process_employee_data(file_path)
        output_file = 'processed_employee_data.csv'
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")