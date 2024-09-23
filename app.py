import gradio as gr
from ocr_processing import perform_ocr, search_keyword
import os

def ocr_and_search(image, keyword):
    image_path = "temp_image.png"
    image.save(image_path)  

    extracted_text = perform_ocr(image_path)  
    search_results = search_keyword(extracted_text, keyword) 

    os.remove(image_path)  
    return extracted_text, search_results

def main():
    with gr.Blocks() as app:
        gr.Markdown("# OCR and Document Search Application")
        gr.Markdown("Upload an image containing text (supports Hindi and English) and search for keywords.")

        with gr.Row():
            image_input = gr.Image(label="Upload Image", type="pil")
            keyword_input = gr.Textbox(label="Keyword to Search")

        with gr.Row():
            ocr_output = gr.Textbox(label="Extracted Text", lines=10)
            search_output = gr.Textbox(label="Search Results", lines=10)

        search_button = gr.Button("Extract Text & Search")
        search_button.click(ocr_and_search, inputs=[image_input, keyword_input], outputs=[ocr_output, search_output])
    # set share true to deploy the app
    app.launch(share=True)

if __name__ == "__main__":
    main()
