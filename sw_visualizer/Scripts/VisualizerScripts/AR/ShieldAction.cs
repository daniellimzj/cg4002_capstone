using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ShieldAction : MonoBehaviour
{

    public Text shieldActionText;
    public Slider slider;
    public Image fill;


    public void SetShieldActionText(int shieldHP)
    {
        shieldActionText.text = shieldHP.ToString();
        slider.value = shieldHP;
    }


}
