using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Shield : MonoBehaviour
{

    public Text shieldText;

    public void SetShieldCount(int shieldCount)
    {
        shieldText.text = shieldCount.ToString();
    }

}
