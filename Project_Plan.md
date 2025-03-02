Project Outline: AI-Supported Animation Software (PoC)

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
        [] o3-mini backend
        [] Make code extractable
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