translation_dict =  {"a":"ka","b":"tu","c":"mi","d":"te","e":"ku","f":"lu","g":"ji","h":"ri","i":"ki","j":"zu","k":"me","l":"ta","m":"rin","n":"to","o":"mo","p":"no","q":"ke","r":"shi","s":"aru","t":"chi","u":"do","v":"ru","w":"mei","x":"na",
            "y":"fu","z":"zi"," ":" "}
name_orig = input("Enter english Name")
name_jap = ""
for i in name_orig:
    name_jap += translation_dict[i.lower()]
print("Japanese Name is",name_jap.capitalize())