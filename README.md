# Codabench Benchmark Submission Guide

Welcome to the Codabench benchmark! In this guide, we will walk you through the process of preparing your submission after your model generates predicted labels for the test set.

### Steps to Submit Your Predictions

1. **Generate Predicted Labels**  
   Once your model generates predicted labels for the test set, ensure that the file containing the predicted labels is in the correct format. The labels file should not have a `.txt` extension, and it should be named `predicted_label`.

2. **Download the `loader.py` Script**  
   To prepare your submission, download the `loader.py` script from this GitHub repo.

3. **Prepare the Submission File**

   - Compress the `loader.py` script and the `predicted_label` file into a single zip file.
   - Make sure that the `predicted_label` file is a plain file without the `.txt` extension.
   - Your zip file should contain both the `loader.py` script and the `predicted_label` file (with no `.txt` extension).

4. **Submit the Zip File**  
   Once you have prepared your zip file with the required contents, you can upload it for evaluation.

---

### Example Structure of Your Submission

Your zip file should have the following structure:

```
/your_submission.zip
  ├── loader.py
  └── predicted_label
```

This structure is crucial to ensure that your submission is properly processed by the benchmark system.
