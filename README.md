# Automated MCQ Generation from Lecture Transcripts

This project presents an innovative approach to enhance the efficiency of generating multiple-choice questions (MCQs) from lecture videos. By utilizing advanced natural language processing techniques, the system extracts keywords and segments lecture transcripts to dynamically formulate targeted MCQs. This project aims to alleviate the burden on educators while ensuring diverse assessment materials for learners.

## Table of Contents
- [Abstract](#abstract)
- [Introduction](#introduction)
- [Literature Review](#literature-review)
- [Assignment Problem](#assignment-problem)
- [Implementation](#implementation)
- [Results and Analysis](#results-and-analysis)
- [Future Works](#future-works)
- [References](#references)

## Abstract
The project leverages advanced NLP techniques to extract keywords from lecture videos, segment transcripts into coherent sections, and generate MCQs to assess comprehension of specific topics covered in the lectures.

## Introduction
The project addresses the challenges of assessing student learning from lecture videos by automating the generation of MCQs. This interdisciplinary research draws from NLP, educational technology, and assessment theory.

## Literature Review
Several studies have informed this project:
1. Systems for automatically creating self-assessment questions within online video lectures.
2. Techniques for transcribing speeches in the Polish Senate.
3. Methods for navigating long lecture videos using visual and audio analysis.

## Assignment Problem
The project involves generating a questionnaire from lecture transcripts using keyword detection. Due to the unavailability of a good dataset, we created a custom dataset using books and the Gemini model.

## Implementation
### Steps:
1. **Dataset Creation**: Generated a dataset using Gemini and custom AI/ML books.
2. **Transcript Extraction**: Used Selenium and the official YouTube API to extract lecture transcripts.
3. **Keyword Extraction**: Utilized NLP techniques and a Random Forest Classifier to identify keywords.
4. **MCQ Generation**: Used the Gemini API to generate MCQs based on extracted keywords.

### Technical Details:
- Python program to gather video links and extract transcripts.
- CountVectorizer and Random Forest Classifier for keyword detection.
- Lemmatization for consistency in keyword extraction.
- Custom dataset and transcripts lemmatized for accurate keyword matching.

## Results and Analysis
- **Random Forest Classifier**:
  - Precision: 0.0588
  - Recall: 0.0092
  - Accuracy: 0.9963
- **NLP Keyword Extraction**: Accuracy varied from 15% to 85%.
- **MCQ Generation**: Successful question generation using the Gemini API.

### Example MCQs:
1. Which term refers to a type of neural network that can generate new data from existing data?
2. What is the name of the optimization algorithm commonly used in deep learning for minimizing loss functions?

## Future Works
Future improvements include utilizing deep learning methods for keyword extraction and transcript segmentation, and expanding the dataset for better accuracy and reliability.

## References
1. Automatic Generation and Insertion of Assessment Items in Online Video Courses by IIT Kharagpur
2. Automatic Keyphrase Extraction and Segmentation Video Lectures by Amrita Vishwa Vidyapeetham
3. System for Automatic Transcription of Sessions of the Polish Senate
4. Erratic Navigation in Lecture Videos Using Hybrid Text-based Index Point Generation by VTU
5. Books by Yoshua Bengio, Nikhil Buduma, Thomas Trappenberg
6. Stanford lecture notes (cs221, cs229, cs230, cs234, cs231, cs4780, ocw6.036, ocw6.s191)
