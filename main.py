
def main():
    for model in urls:

        blob = scrape_model_hub(url)

        provenance = get_provenance(blob)
        reproducibility = get_reproducibility(blob)
        portability = get_portability(blob)

        print(provenance, reproducibility, portability)

if __name__ == '__main__':
    main()
