# 🎬 AI Product Video Bot

Transform your product images into stunning AI-generated video ads in seconds!

## Features

✨ **AI-Powered Script Generation** - Uses Claude AI to create compelling marketing scripts
🎥 **Multiple Video Engines** - Supports Runway AI and Synthesia for video generation
📸 **Easy Image Upload** - Simply upload your product images
🎨 **Customizable Styles** - Choose from cinematic, modern, professional, trendy, or minimal styles
⚡ **Fast Generation** - Get your video ads ready to upload in minutes
💾 **Download Support** - Export your generated videos with one click

## Tech Stack

- **Backend:** Flask (Python)
- - **AI Models:** Claude 3.5 Sonnet, Runway AI, Synthesia
  - - **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
    - - **APIs:** Anthropic, Runway ML, Synthesia
     
      - ## Installation
     
      - ### Prerequisites
      - - Python 3.8+
        - - API keys for:
          -   - Anthropic (Claude)
              -   - Runway ML
                  -   - Synthesia
                   
                      - ### Setup
                   
                      - 1. Clone the repository:
                        2. ```bash
                           git clone https://github.com/haleem2212/ai-product-video-bot.git
                           cd ai-product-video-bot
                           ```

                           2. Create a virtual environment:
                           3. ```bash
                              python -m venv venv
                              source venv/bin/activate  # On Windows: venv\Scripts\activate
                              ```

                              3. Install dependencies:
                              4. ```bash
                                 pip install -r requirements.txt
                                 ```

                                 4. Create `.env` file with your API keys:
                                 5. ```
                                    ANTHROPIC_API_KEY=your_anthropic_key
                                    RUNWAY_API_KEY=your_runway_key
                                    SYNTHESIA_API_KEY=your_synthesia_key
                                    ```

                                    5. Run the application:
                                    6. ```bash
                                       python ai_video_bot.py
                                       ```

                                       6. Open your browser and navigate to:
                                       7. ```
                                          http://localhost:5000
                                          ```

                                          ## Usage

                                          1. **Enter Product Information**
                                          2.    - Product name
                                                -    - Product description
                                                     -    - Key features
                                                      
                                                          - 2. **Upload Product Image**
                                                            3.    - Click upload to select your product image
                                                                  -    - Supported formats: PNG, JPG, JPEG, GIF, WebP
                                                                   
                                                                       - 3. **Select Video Style**
                                                                         4.    - Choose from available video styles
                                                                               -    - Cinematic, Modern, Professional, Trendy, Minimal
                                                                                
                                                                                    - 4. **Generate Script**
                                                                                      5.    - Click "Generate Ad Script" button
                                                                                            -    - AI will create a compelling marketing script
                                                                                             
                                                                                                 - 5. **Generate Video**
                                                                                                   6.    - Click "Generate Video" button
                                                                                                         -    - Wait for video generation to complete
                                                                                                              -    - Preview and download your video
                                                                                                               
                                                                                                                   - ## API Endpoints
                                                                                                               
                                                                                                                   - ### Upload Image
                                                                                                                   - - **POST** `/api/upload`
                                                                                                                     - - Upload product image for processing
                                                                                                                      
                                                                                                                       - ### Generate Script
                                                                                                                       - - **POST** `/api/generate-script`
                                                                                                                         - - Generate marketing script using Claude AI
                                                                                                                          
                                                                                                                           - ### Generate Video
                                                                                                                           - - **POST** `/api/generate-video`
                                                                                                                             - - Create AI video from image and script
                                                                                                                              
                                                                                                                               - ## Project Structure
                                                                                                                              
                                                                                                                               - ```
                                                                                                                                 ai-product-video-bot/
                                                                                                                                 ├── ai_video_bot.py          # Main Flask application
                                                                                                                                 ├── requirements.txt          # Python dependencies
                                                                                                                                 ├── templates/
                                                                                                                                 │   └── index.html           # Web interface
                                                                                                                                 ├── uploads/                 # Uploaded images
                                                                                                                                 ├── videos/                  # Generated videos
                                                                                                                                 └── README.md               # This file
                                                                                                                                 ```
                                                                                                                                 
                                                                                                                                 ## Configuration
                                                                                                                                 
                                                                                                                                 ### Environment Variables
                                                                                                                                 
                                                                                                                                 ```
                                                                                                                                 ANTHROPIC_API_KEY      # Your Anthropic API key
                                                                                                                                 RUNWAY_API_KEY        # Your Runway ML API key
                                                                                                                                 SYNTHESIA_API_KEY     # Your Synthesia API key
                                                                                                                                 ```
                                                                                                                                 
                                                                                                                                 ### Flask Configuration
                                                                                                                                 
                                                                                                                                 - **MAX_CONTENT_LENGTH** - Maximum upload size: 500MB
                                                                                                                                 - - **DEBUG** - Enabled for development (disable for production)
                                                                                                                                   - - **PORT** - Default: 5000
                                                                                                                                    
                                                                                                                                     - ## Troubleshooting
                                                                                                                                    
                                                                                                                                     - ### Video Not Generating
                                                                                                                                     - - Check API key validity
                                                                                                                                       - - Ensure image format is supported
                                                                                                                                         - - Verify API service status
                                                                                                                                          
                                                                                                                                           - ### Upload Fails
                                                                                                                                           - - Check file size (max 500MB)
                                                                                                                                             - - Verify image format
                                                                                                                                               - - Check browser console for errors
                                                                                                                                                
                                                                                                                                                 - ### Script Generation Issues
                                                                                                                                                 - - Verify Anthropic API key
                                                                                                                                                   - - Check internet connection
                                                                                                                                                     - - Review error message in browser
                                                                                                                                                      
                                                                                                                                                       - ## Future Enhancements
                                                                                                                                                      
                                                                                                                                                       - - [ ] Batch video processing
                                                                                                                                                         - [ ] - [ ] Custom music selection
                                                                                                                                                         - [ ] - [ ] Multiple language support
                                                                                                                                                         - [ ] - [ ] Video editing interface
                                                                                                                                                         - [ ] - [ ] Template library
                                                                                                                                                         - [ ] - [ ] Social media integration
                                                                                                                                                         - [ ] - [ ] Analytics dashboard
                                                                                                                                                         - [ ] - [ ] Premium plan features
                                                                                                                                                        
                                                                                                                                                         - [ ] ## Security Considerations
                                                                                                                                                        
                                                                                                                                                         - [ ] - Never commit `.env` file with real API keys
                                                                                                                                                         - [ ] - Use environment variables for sensitive data
                                                                                                                                                         - [ ] - Validate all file uploads
                                                                                                                                                         - [ ] - Implement rate limiting for production
                                                                                                                                                         - [ ] - Use HTTPS in production
                                                                                                                                                        
                                                                                                                                                         - [ ] ## Performance Tips
                                                                                                                                                        
                                                                                                                                                         - [ ] - Keep image size under 5MB for faster processing
                                                                                                                                                         - [ ] - Use modern browsers (Chrome, Firefox, Safari, Edge)
                                                                                                                                                         - [ ] - Check internet connection quality
                                                                                                                                                         - [ ] - Close other applications for faster generation
                                                                                                                                                        
                                                                                                                                                         - [ ] ## Contributing
                                                                                                                                                        
                                                                                                                                                         - [ ] Contributions are welcome! Please feel free to submit a Pull Request.
                                                                                                                                                        
                                                                                                                                                         - [ ] 1. Fork the repository
                                                                                                                                                         - [ ] 2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
                                                                                                                                                         - [ ] 3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
                                                                                                                                                         - [ ] 4. Push to the branch (`git push origin feature/AmazingFeature`)
                                                                                                                                                         - [ ] 5. Open a Pull Request
                                                                                                                                                        
                                                                                                                                                         - [ ] ## License
                                                                                                                                                        
                                                                                                                                                         - [ ] This project is licensed under the MIT License - see the LICENSE file for details.
                                                                                                                                                        
                                                                                                                                                         - [ ] ## Disclaimer
                                                                                                                                                        
                                                                                                                                                         - [ ] This tool generates videos using third-party AI APIs. Ensure you have the right to use generated content commercially. Review each API's terms of service for usage rights and limitations.
                                                                                                                                                        
                                                                                                                                                         - [ ] ## Support
                                                                                                                                                         - [ ] 
                                                                                                                                                         For issues, questions, or suggestions:
- Open an issue on GitHub
- - Check existing documentation
  - - Review error logs
   
    - ## Acknowledgments
   
    - - Claude AI by Anthropic
      - - Runway ML for video generation
        - - Synthesia for avatar videos
          - - Flask framework
            - - Community contributors
             
              - ---

              Made with ❤️ for creators and entrepreneurs
