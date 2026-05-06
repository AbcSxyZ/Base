## Open Models Knowledge Base

Knowledge base to explore and learn about Open Science, Open Education, Open Software, Open Hardware, Open Standard and
all things open.

Website : [open-models.org](https://open-models.org)

Information to enable set up of the website (based on [Quarto](https://quarto.org/)). [Contribution
guidelines](organisation/contribution-guidelines.md) and
[project roadmap](organisation/roadmap.md) are shared directly on the website.

### Installation guideline

1/ Clone the git repository.

2/ Install Quarto (see instructions on [tool website](https://quarto.org/docs/get-started/))

*Using Ubuntu/Debian (check website to select last version)*
```bash
wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.9.37/quarto-1.9.37-linux-amd64.deb 

sudo apt install ./quarto-1.9.37-linux-amd64.deb 

# You shoud be able to access quarto CLI, test with:
quarto -v
```

Move to the git folder and render the website using `quarto render`.

Alternatively, you can get render and display a local instance of the website using `quarto preview`.

You can now have your local knowledge base!

### License

All resources in this knowledge base are dedicated to the public domain under [CC0 1.0 Universal](LICENSE) — you are free to use, modify, and share them without restriction and permission.
