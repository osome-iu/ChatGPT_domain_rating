# Introduction

This repo contains the code and data for the paper "Large language models can rate news outlet credibility."

We use the following data in our study:

| Data | Location | Note |
|------|----------|------|
| Aggregate domain rating list from Lin et al. | https://github.com/hauselin/domain-quality-ratings | Please download the data in their repo. |
| MBFC ratings | [/data/mbfc_ratings.csv](/data/mbfc_ratings.csv) | We collected the data and share it here. |
| NewsGuard ratings | N/A | The data is proprietary, please contact newsguardtech.com to license the data. |
| ChatGPT ratings | [/data/chatgpt_ratings.csv.gz](/data/chatgpt_ratings.csv.gz) | We share the responses from ChatGPT here. |
| Tranco list | https://tranco-list.eu | Please download the data from their website. |

We also share the script we used to query the ChatGPT API at [/scripts/query_domain_credibility.py](/scripts/query_domain_credibility.py).
You will need an OpenAI API key, which can be applied at https://platform.openai.com .

# Citation

If you use our data or code in your research, please cite our work as follows:

```bib
@article{yang2023large,
  title={Large language models can rate news outlet credibility},
  author={Yang, Kai-Cheng and Menczer, Filippo},
  journal={Preprint},
  year={2023}
}
```
