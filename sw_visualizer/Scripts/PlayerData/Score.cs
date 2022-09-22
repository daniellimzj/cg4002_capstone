using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Score : MonoBehaviour
{
    public Text scoreText;

    public int playerScore, opponentScore;

    void Start()
    {
        playerScore = 0;
        opponentScore = 0;
        SetScoreText();
    }

    public void SetScoreText()
    {
        scoreText.text = playerScore.ToString() + " : " + opponentScore.ToString();
    }

    public void ChangePlayerScore()
    {
        playerScore++;
        SetScoreText();
    }

    public void ChangeOpponentScore()
    {
        opponentScore++;
        SetScoreText();
    }
}
