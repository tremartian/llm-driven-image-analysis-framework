# -llm-driven-image-analysis-framework
LLM-Driven Image Analysis Framework


**LLM-Driven Image Analysis Framework** is a modular, Python-based tool designed to facilitate the rapid development of customized image analysis workflows. It leverages large language models (LLMs) to automatically generate both user interfaces and backend code, simplifying the creation of analysis modules for domain experts with limited programming expertise. The framework supports the integration of diverse image processing methods and allows researchers to build and test tailored analysis pipelines with minimal coding overhead.

---

## Features

* **Modular Design:** Supports easy integration of new image processing modules.
* **LLM-Generated Code:** Automatically generates functional Python code and JSON-based user interface definitions from structured prompts.
* **Customizable Workflows:** Enables users to define workflows without extensive programming.
* **Support for Multiple Domains:** Initially tested with grain analysis and plywood detection, but adaptable to other scientific and industrial contexts.
* **Graphical User Interface:** Built with Tkinter for parameter selection, method chaining, and image visualization.
* **Data Analysis Support:** Integrated CSV export and basic statistical visualization (e.g., histograms).

---

## Installation

Clone this repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/llm-driven-image-analysis-framework.git
cd llm-driven-image-analysis-framework
pip install -r requirements.txt
```

---

## Usage

1. **Start the Application:**

   ```bash
   python A_Main.py
   ```

2. **Load an Image:**

   * Select an image file for analysis using the GUI.

3. **Choose a Processing Method:**

   * Select available image processing methods (e.g., Brightness Adjustment, Segmentation).
   * Adjust parameters using the interactive sliders and dropdowns.

4. **Run Analysis:**

   * View processed images and intermediate results.
   * Optionally export analysis results to a CSV file.

5. **Analyze Results:**

   * Navigate to the **Results** tab.
   * Zoom in/out of images and visualize statistical data from CSV exports.

---

## Framework Structure

* `methods/`: Contains modular Python functions for image processing.
* `config/`: JSON configurations for UI and processing methods.
* `SharedState.py`: Manages shared state between tabs and methods.
* `A_Main.py`: Main application entry point.
* `Tabs/`: Contains individual tabs (methods, results) for GUI integration.

---

## Contributing

Contributions are welcome! Please open issues or pull requests for:

* New image processing modules.
* Enhancements to the user interface.
* Additional test cases or documentation improvements.

---

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.

---


