from pyscript import display

subject = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
def general_weighted_average(e):

    science = float(document.getElementById('science').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    filipino = float(document.getElementById('filipino').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)

    units_subject = (5, 3, 2, 1)
    
    weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units

    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    summary = f"""{subject[0]}: {science:.0f}
{subject[1]}: {math:.0f}
{subject[2]}: {english:.0f}
{subject[3]}: {filipino:.0f}
{subject[4]}: {ict:.0f}
{subject[5]}: {pe:.0f}"""

    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')