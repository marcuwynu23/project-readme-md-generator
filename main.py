# Function to generate README content
def generate_readme(data):
    return '''<div align="center">

# {} 

[![GitHub license](https://img.shields.io/github/license/{}/{})](https://github.com/{}/{}blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/{}/{}?style=flat)](https://github.com/{}/{}stargazers)
[![GitHub issues](https://img.shields.io/github/issues/{}/{}?style=flat)](https://github.com/{}/{}issues)

</div>

{}

## Features

{}

## Technologies Used

{}

## Getting Started

{}

## Usage

{}

## Contribution

{}

## License

This project is licensed under the {} License - see the [LICENSE](LICENSE) file for details.
'''.format(data['title'], data['username'], data['repository'], data['username'], data['repository'], data['username'], data['repository'], data['username'], data['repository'], data['username'], data['repository'], data['username'], data['repository'], data['username'], data['repository'], data['description'], '\n'.join([f"- {feature}" for feature in data['features']]), '\n'.join([f"- {tech}" for tech in data['technologies']]), data['getting_started'], data['usage'], data['contribution'], data['license'])

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
        'contribution': input('Enter contribution guidelines: '),
        'license': input('Enter project license: ')
    }
    return data

# Main function


def main():
    data = collect_input()
    readme_content = generate_readme(data)
    write_readme(readme_content)


if __name__ == "__main__":
    main()
