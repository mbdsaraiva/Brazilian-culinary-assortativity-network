![Project Banner](/banner/banner.png)

<h1 align="center">Brazilian Culinary Network Assortativity 🍲</h1>


## 👤 Author

*   **Name:** Matheus Bezerra Dantas Saraiva
*   **Course:** Algorithms and Data Structures II

## 📝 Project Description

This project aims to analyze the assortativity of a co-occurrence network of ingredients from popular Brazilian recipes. The main goal is to determine whether Brazilian cuisine tends to favor homogeneous combinations (ingredients of the same type) or heterogeneous combinations (ingredients of different types).

The analysis involves:
1.  Identifying and classifying ingredients by type (e.g., Protein, Carbohydrate, Vegetable).
2.  Building an ingredient co-occurrence graph from at least 50 popular Brazilian recipes.
3.  Calculating the assortativity coefficient based on ingredient types using NetworkX.
4.  Visualizing the network graph.
5.  Discussing the findings regarding ingredient pairing preferences in Brazilian cuisine.

**Video Presentation:** [link](https://drive.google.com/file/d/130wfXjWs-9fsDicOq2Ituwj5rQ6EnuOh/view).

## 🛠️ Methodology

* **Image Sources:** All recipe images were sourced from [TudoGostoso](https://www.tudogostoso.com.br/).
* **Data Collection:** ChatGPT4 was used to suggest 50 popular Brazilian recipes for the project.
*   **Ingredient Extraction & Classification:** ChatGPT4 and Microsoft Copilot were utilized to extract ingredients from recipe images and classify them into predefined categories (Protein, Carbohydrate, Vegetable, Fruit, Dairy, Fat, Condiment, Other). Details on the specific LLMs and prompts used can be found in the `llm_info.md` file.
* **Data Structuring:** The collected data (recipe, ingredients, types) was organized into a `.csv` file (`recipes.csv`) using ManusAI.
*   **Network Construction:** A graph was built using the NetworkX library in Python, where nodes represent ingredients and edges connect ingredients that appear together in the same recipe. Ingredient types were assigned as node attributes.
*   **Assortativity Analysis:** The attribute assortativity coefficient was calculated based on the 'type' attribute to measure the tendency of nodes to connect to others with the same type.
*   **Network Visualization:** The graph was visualized using Matplotlib, with node colors representing ingredient types and node sizes proportional to their degree (number of connections).

## 📊 Network Graph

Below is the visualization of the Brazilian ingredient co-occurrence network. Nodes represent ingredients, colored by type, and sized by their degree (number of connections). Edges link ingredients appearing in the same recipe.

![Ingredient Network Graph](/network_images/network.png)

## 📈 Results and Discussion

The analysis of the Brazilian culinary ingredient network revealed several key insights:

*   **Network Size:** The graph consists of **78 unique ingredients** (nodes) and **327 connections** (edges) between them, derived from 50 recipes.
*   **Network Density:** The network has a density of approximately **0.1089**, indicating that about 10.9% of all possible connections between ingredients exist in this dataset.
*   **Assortativity Coefficient:** The calculated attribute assortativity coefficient based on ingredient type is **-0.0794**. 
*   **Interpretation (Heterophily):** A negative assortativity coefficient suggests **heterophily**. This means that in Brazilian cuisine, based on this dataset, there is a slight preference for connecting ingredients of *different* types rather than the same type. Ingredients tend to pair with ingredients from other categories (e.g., Protein with Vegetable, Vegetable with Carbohydrate).
*   **Co-occurrence Analysis:** This heterophilic tendency is further supported by the co-occurrence data:
    *   Connections between different types (Heterophily): **86.54%**
    *   Connections between the same type (Homophily): **13.46%**
*   **Most Frequent Combinations:** The most common pairings involve Vegetables connecting with Proteins (9.48%), other Vegetables (8.87%), and Carbohydrates (7.65%).
*   **Central Ingredients:** The most central ingredients (highest degree) are fundamental components often used as bases or seasonings in Brazilian cooking:
    *   Onion (Vegetable): 38 connections
    *   Garlic (Condiment): 28 connections
    *   Tomato (Vegetable): 27 connections
    *   Pepper (Condiment): 27 connections
    *   Bell Pepper (Vegetable): 20 connections
*   **Ingredient Type Connectivity:** Vegetables show the highest average degree (12.29), indicating they are frequently combined with many other ingredients. Proteins (7.39) and Carbohydrates (7.00) also show significant connectivity.
*   **Network Structure:** The network is fully connected (1 connected component) with a diameter of 6 and an average shortest path length of 2.58, suggesting ingredients are relatively closely linked within the culinary network.

**Discussion:**

The negative assortativity coefficient (-0.0794) points towards a preference for **heterophily** in the analyzed Brazilian recipes. This indicates that Brazilian cuisine, as represented by this dataset, tends to combine ingredients from different functional categories (like pairing a protein with a vegetable or carbohydrate) more often than ingredients from the same category (like pairing two different types of vegetables). This contrasts with homophilic networks where nodes tend to connect to similar nodes. The high percentage of heterophilic connections (86.54%) strongly reinforces this finding.

The central role of ingredients like onion, garlic, and tomato (all with high degrees) highlights their importance as foundational elements that bridge different ingredient types. Vegetables, as a category, have the highest average degree, suggesting they are versatile connectors in Brazilian dishes, frequently appearing alongside proteins, carbohydrates, and condiments.

The frequent co-occurrence of Vegetable + Protein and Vegetable + Carbohydrate aligns with the common structure of Brazilian meals, often featuring a protein source, a carbohydrate source, and accompanying vegetables or salads. While there is some homophily (13.46%), particularly within the Vegetable category itself (Vegetable + Vegetable is the second most frequent combination), the overall trend leans towards creating contrast and balance by pairing ingredients from distinct groups. This suggests that the richness and complexity of Brazilian cuisine might stem, in part, from this tendency to combine diverse ingredient types, creating balanced and flavorful dishes rather than relying heavily on combinations within the same category.

## ▶️ How to Run

To replicate the analysis and generate the network graph:

1.  **Clone the repository:**
    ```bash
      git clone https://github.com/mbdsaraiva/brazilian-culinary-network-assortativity.git
      cd brazilian-culinary-network-assortativity
    ```
2.  **Ensure you have Python installed.**
3.  **Install required libraries:**
    ```bash
    pip install pandas networkx matplotlib numpy
    ```
4.  **Place the dataset file:** Make sure the `recipes.csv` file is in the same directory as the script, or update the `file_path` variable in the script (`main.py`) accordingly.
5.  **Run the script:**
    ```bash
    python main.py 
    ```
    (Or execute the cells in the `main.py` notebook if using Jupyter).

This will print the analysis results (assortativity coefficient, network metrics, top ingredients, etc.) to the console and display the network graph visualization.

## 📁 Repository Structure

The repository includes the following key files and directories:

*   `README.md`: This file, providing an overview of the project.
*   `recipes.csv`: The dataset containing recipes, ingredients, and their types.
*   `main.py`: The Python code used for data loading, network construction, analysis, and visualization.
*   `/images/`: Directory containing generated images, such as the network graph (`network.png`).
*   `/network_images/`: Directory containing the network graph (`network.png`) and the `nxviz.png`.
*   `llm_info.md`: Document detailing the Language Models and prompts used in the project.

## 🤖 LLM Information

Details about the Language Models (ChatGPT 4.0, Microsoft Copilot, Manus AI) and the specific prompts used for ingredient extraction and classification are available in the `llm_info.md` file.


