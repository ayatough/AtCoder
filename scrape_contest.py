def main(contest_name: str):
    from pathlib import Path
    import requests
    from bs4 import BeautifulSoup

    top_url = f"https://atcoder.jp/contests/{contest_name}"
    tasks_url = f"https://atcoder.jp/contests/{contest_name}/tasks"
    response = requests.get(tasks_url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    folder = Path(contest_name.upper())
    folder.mkdir(exist_ok=True)

    problem_table = soup.select('h2:-soup-contains("Tasks") ~ div > table')[0]
    table_row = problem_table.find("tbody")
    while table_row := table_row.find_next("tr"):
        cell = table_row.find_next("td")
        a = cell.find_next("a")
        task_url_sub = Path(a["href"]).stem
        task_title = a.get_text(strip=True)

        cell = cell.find_next("td")
        task_name = cell.find_next("a").get_text(strip=True)
        print(task_url_sub, task_title, task_name)

        task_response = requests.get(tasks_url + "/" + task_url_sub)
        task_html = task_response.text
        task_soup = BeautifulSoup(task_html, "html.parser")
        sample_input_elems = task_soup.select(f'h3:-soup-contains("Sample Input ")')
        sample_output_elems = task_soup.select(f'h3:-soup-contains("Sample Output ")')
        for sample_input_elem, sample_output_elem in zip(sample_input_elems, sample_output_elems):
            i_sample = int(sample_input_elem.get_text(strip=True).split(" ")[-1])
            input_txt = sample_input_elem.find_next("pre").get_text()
            output_txt = sample_output_elem.find_next("pre").get_text()

            print(i_sample)
            input_file = folder / f"test_{task_title}_{i_sample}"
            output_file = folder / f"ans_{task_title}_{i_sample}"
            with open(input_file, "w") as f:
                f.writelines(input_txt)
            with open(output_file, "w") as f:
                f.writelines(output_txt)

        # i_sample = 1
        # # print(task_soup)
        # while sample_input := task_soup.select(f'h3:-soup-contains("Sample Input {i_sample}") ~ pre'):
        #     print(sample_input[0].get_text())
        #     i_sample += 1



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="contest_name")
    args = parser.parse_args()
    main(**vars(args))
