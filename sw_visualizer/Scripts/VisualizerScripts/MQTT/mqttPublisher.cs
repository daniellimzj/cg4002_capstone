using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using M2MqttUnity;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;
using System.Diagnostics;

public class mqttPublisher : M2MqttUnityClient
{

    public string nameController = "Controller 1";
    public string topicPublish = "b11/is_in_same_area"; // topic to publish


    // Start is called before the first frame update
    protected override void Start()
    {
        base.Start();
    }

    public void TESTSEND_yes()
    {
        UnityEngine.Debug.Log("inside test send yes");
        string messagePublish = "1";
        client.Publish(topicPublish, System.Text.Encoding.UTF8.GetBytes(messagePublish), MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
    }

    public void TESTSEND_no()
    {
        UnityEngine.Debug.Log("inside test send no");
        string messagePublish = "0";
        client.Publish(topicPublish, System.Text.Encoding.UTF8.GetBytes(messagePublish), MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
    }



}