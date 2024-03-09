 
# Function to generate README content
def generate_readme(data):
    return f'''<div align="center">

# {data['title']} 

[![GitHub license](https://img.shields.io/github/license/{data['username']}/{data['repository']})](https://github.com/{data['username']}/{data['repository']}/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/{data['username']}/{data['repository']})](https://github.com/{data['username']}/{data['repository']}/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/{data['username']}/{data['repository']})](https://github.com/{data['username']}/{data['repository']}/issues)

</div>

{data['description']}

## Features

{'\n'.join([f"- {feature}" for feature in data['features']])}

## Technologies Used

{'\n'.join([f"- {tech}" for tech in data['technologies']])}

## Getting Started

{data['getting_started']}

## Usage

{data['usage']}

## Contribution

{data['contribution']}

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
'''

# Function to write README file
def write_readme(content):
    with open('README.md', 'w') as f:
        f.write(content)
    print('README.md file created successfully!')

# Function to collect user input
def collect_input():
    data = {
        'username': input('Enter your GitHub username: '),
        'repository': input('Enter your repository name: '),
        'title': input('Enter project title: '),
        'description': input('Enter project description: '),
        'features': input('Enter project features (separated by commas): ').split(','),
        'technologies': input('Enter technologies used (separated by commas): ').split(','),
        'getting_started': input('Enter getting started guide: '),
        'usage': input('Enter usage instructions: '),
        'contribution': input('Enter contribution guidelines: ')
    }
    return data

# Main function
def main():
    data = collect_input()
    readme_content = generate_readme(data)
    write_readme(readme_content)

if __name__ == "__main__":
    main()
