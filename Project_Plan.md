Project Outline: AI-Supported Animation Software (PoC)

= SPEC-1: AI-Supported Animation Software
:sectnums:
:toc:

== Background

The process of creating animations with Manim is powerful but time-consuming, requiring precise scripting and mathematical transformations. While tools like Adobe After Effects offer intuitive interfaces, they lack Manim’s mathematically precise control.

This project aims to bridge the gap between scripting-based animation and creative sketching by introducing an AI-assisted workflow. The software will allow users to sketch vector-based shapes and provide text-based prompts, which an AI model will convert into Manim animation scripts. 

Initially, the proof-of-concept (PoC) version will focus on:
- **Targeting experienced Manim programmers**, ensuring they can refine AI-generated scripts.
- **Generating raw Manim code only**, without real-time preview adjustments.
- **Providing a simple sketchpad interface**, allowing users to draw vector shapes that serve as a basis for AI-generated animations.


Phase 1: Project Setup & Basic UI

    [x] Set up a Git repository (e.g., GitHub/GitLab).
    [x] Initialize a Python environment with Flask/FastAPI.
    [x] Set up a basic frontend with Fabric.js (a simple HTML page with a canvas).
    [x] Implement basic shape drawing (e.g., circles, rectangles, paths).
    [x] Add a button to send vector data to the backend.

Phase 2: Backend Development & AI Integration

    [x] Set up Flask/FastAPI API to handle sketchpad data.
    [] Integrate LangChain for AI-powered Manim code generation.
        [x] Basic prompt and functionality
        [x] GPT-4o backend
        [x] o1-mini backend
        [x] Make code extractable
    [] Run generated manim scripts in a backend service
    [] Define structured AI prompts for converting vector shapes to Manim code.
    [] Implement API routes for text prompt + vector data processing.
    [] Test AI-generated Manim scripts manually.

Phase 3: UI Enhancements & Refinements

    [] Add a basic code editor (e.g., Monaco or simple textarea).
    [] Display AI-generated Manim scripts in the editor.
    [] Allow users to manually refine the script.
    [] Implement a "Download Manim Script" button.
    [] Improve UI styling and usability.

Phase 4: Testing & Iteration

    [] Test AI generation quality with various sketches + prompts.
    [] Optimize prompt engineering for better Manim script output.
    [] Fix bugs & improve stability.
    [] Optimize backend performance (e.g., handling multiple requests).
    [] Document API endpoints and usage.

Phase 5: Deployment & Feedback

    [] Deploy the PoC version (e.g., on a simple cloud server or local app).
    [] Collect user feedback from experienced Manim users.
    [] Identify areas for further improvement (e.g., real-time preview, better AI refinements).