using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Score : MonoBehaviour
{
    public Text scoreText;

    public int playerScore, opponentScore;

    public void UpdateScore(int d1, int d2)
    {
        playerScore = d1;
        opponentScore = d2;
        SetScoreText();
    }

    public void UpdatePlayerScore(int d1)
    {
        playerScore = d1;
        SetScoreText();
    }

    public void UpdateOpponentScore(int d2)
    {
        playerScore = d2;
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
