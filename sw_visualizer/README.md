# Software Visualizer 

## Project Description  
The Software Visualizer gives players a direct and feedback of the of the game play status.  

---

## Installation and Setup 
### Download
- Unity: https://unity3d.com/get-unity/download
- Vuforia: https://developer.vuforia.com/downloads/sdk

### Setting up
- Unity: https://learn.unity.com/tutorial/install-the-unity-hub-and-editor
- Vuforia: https://library.vuforia.com/getting-started/getting-started-vuforia-engine-unity

---

## Usage
1. Build Unity Project
- In Unity, go to `File` - `Build Settings` - `Build`
2. Install to iPhone
- In Finder, go to `output` - `Unity-iPhone`
- Open Unity-iPhone.xcodeproj in Xcode
- Configure `Signing & Capabilities` by checking the `Automatically manage signing`
- Build and install the project onto iPhone


---

## Libraries used
1. Vuforia  
- Software development kit (SDK) for creating Augmented Reality apps.
- Enables marker detection and the anchoring of AR effects.
2. UnityEngine.UI
- Provides UI module implementations with basic components which are required for Unity’s UI system render.
- This will be used to create overlay UI graphics in the game screen and make sure it does not block the camera feeds.
3. M2MqttUnityClient
- MQTT Unity package which allows the user to communicate with MQTT broker service.
- Able to publish and subscribe on multiple different topics.




