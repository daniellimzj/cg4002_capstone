using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ChangeScene : MonoBehaviour
{
    public static string playerid;

    public void LoadARScenePlayer1()
    {
        playerid = "p1";
        SceneManager.LoadScene("ARScene");
    }

    public void LoadARScenePlayer2()
    {
        playerid = "p2";
        SceneManager.LoadScene("ARScene");
    }

    public void ExitApp()
    {
        Application.Quit();
        Debug.Log("You have quit the app");
    }

    public void LoadMenuScene()
    {
        SceneManager.LoadScene("MenuScene");
    }

    
}
