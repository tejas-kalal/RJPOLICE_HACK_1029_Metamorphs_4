import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
print('AI/ML System for Enhanced FIR Generation and Section Recommendation')
text = input('Brief description of offence:')
section = ''
def get_crime_type(text):
    # Download stopwords if not already downloaded
    #nltk.download('stopwords')
    
    # Download punkt if not already downloaded
    #nltk.download('punkt')
    
    # Load the stopwords
    stop_words = set(stopwords.words('english'))
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Define a list of crime keywords
    crime_keywords_sedition = ['sedition']
    crime_keywords_rioting = ['rioting','anarchy','anarching','anarchist']
    crime_keywords_affray = ['affraying','fighting','battle']
    crime_keywords_murder = ['murder','kill','murdered','killed','headoffed','chopped','dead']
    crime_keywords_suicide = ['suicide','killself','self-harm']
    crime_keywords_acid = ['acid']
    crime_keywords_hurt = ['hurt','beat','hurted','smashed','harm','injury']
    crime_keywords_sexual = ['raped','sexual','intercourse','sex','fuck','fucked','slepped','sleep','slept']
    crime_keywords_kidnapping = ['kidnapped','kidnapping','abduction']
    crime_keywords_theft = ['stolen','steal','theft','thief']
    # Check if any crime keyword is present in the filtered tokens
    for word in filtered_tokens:
        if word.lower() in crime_keywords_sedition:
            word = 'sedition'
            return word.lower()
        elif word.lower() in crime_keywords_rioting:
            word = 'rioting'
            return word.lower()
        elif word.lower() in crime_keywords_affray:
            word = 'affray'
            return word.lower()
        elif word.lower() in crime_keywords_murder:
            word = 'murder'
            return word.lower()
        elif word.lower() in crime_keywords_suicide:
            word = 'suicide'
            return word.lower()
        elif word.lower() in crime_keywords_acid:
            word = 'acid attack'
            return word.lower()
        elif word.lower() in crime_keywords_hurt:
            word = 'voluntarily causing hurt'
            return word.lower()
        elif word.lower() in crime_keywords_sexual:
            word = 'sexual harassment '
            return word.lower()
        elif word.lower() in crime_keywords_kidnapping:
            word = 'kidnapping'
            return word.lower()
        elif word.lower() in crime_keywords_theft:
            word = 'theft'
            return word.lower()
        
    
    # If no crime keyword is found, return None
    return None

# Example usage
crime_type = get_crime_type(text)
print(f'Identified Offence : {crime_type}')

if crime_type == 'sedition':
    section = 'IPC Section 124-A'
elif crime_type == 'rioting':
    section = 'IPC Section 147'
elif crime_type == 'affray':
    section = 'IPC section 160'
elif crime_type == 'murder':
    section = 'IPC Section 302'
elif crime_type == 'suicide':
    section = 'IPC Section 309'
elif crime_type == 'acid attack':
    section = 'IPC Section 326-B'
elif crime_type == 'voluntarily causing hurt':
    section = 'IPC Section 323'
elif crime_type == 'sexual harassment ':
    section = 'IPC Section 354 354-A and 376 can be used accordingly'
elif crime_type == 'kidnapping':
    section = 'IPC Section 359'
elif crime_type == 'theft':
    section = 'IPC Section 378'
else:
    print('Sorry! Cant suggest section.')

print(f'Suggested section : {section}\n\n')


#code that will Generate FIR
opinion = input('Do you wanted to generate FIR(yes/no):')
if opinion == 'yes':
    print('\n\nPlease provide Following Deatails\n')
    Police_Station = 'Jaipur'
    District= 'Jaipur'
    No = '001'
    Datehour_of_Occurrence = input('\nEnter Date & hour of Occurrence: ')
    Datehour_when_reported = input('\nEnter Date & hour of reported: ')
    Name_of_complainant = input('\nEnter name of complainant or informer: ')
    residence_of_complainant = input('\nEnter residence of complainant or informer: ')
    Place_of_occurence = input('\nPlace of occurence ? ')
    distance_direction = input('\ndistance & direction from the Police Station : ')
    Name_of_Criminal = input('\nEnter name of Criminal : ')
    Address_of_criminal = input('\nEnter Address of criminal : ')
    print('_______________________________________________________________________________________')
    print('\n\nAI Generated FIR')
    print('_______________________________________________________________________________________')
    print(f'\nPolice station: {Police_Station} District: {District} No: {No}')
    print(f'\n1.Date and Hour of occurence :{Datehour_of_Occurrence}')
    print(f'\n2.Name and residence of informer and complainant: {Name_of_complainant} {residence_of_complainant}')
    print(f'\n3.Brief description of offence (with section):{text} {section}')
    print(f'\n4.Place of occurence and distance and direction from the Police Station:{Place_of_occurence} {distance_direction}')
    print(f'\nName & Address of the Criminal: {Name_of_Criminal} {Address_of_criminal}')
    print('_______________________________________________________________________________________')
    print('\nHappy to help you !')
elif opinion == 'no':
    print('\nHappy to help !')
else:
    print('Enter valid input !')