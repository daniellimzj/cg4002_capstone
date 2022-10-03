using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Grenade : MonoBehaviour
{
    public Text grenadeText;

    public void SetGrenadeCount(int grenadeCount)
    {
        grenadeText.text = grenadeCount.ToString();
    }
}
