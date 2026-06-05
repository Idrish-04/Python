from countries_data import country
languages=set()
for item in country:
    for language in item["languages"]:
        languages.add(language)

print("Total number of languages:", len(languages))
language_count = {}

for item in country:
    for language in item["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

top_languages = sorted(
    language_count.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]

print("Ten most spoken languages:")
for language, count in top_languages:
    print(language, count)