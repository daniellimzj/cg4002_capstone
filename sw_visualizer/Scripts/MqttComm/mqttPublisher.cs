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
    public string tagOfTheMQTTReceiver = "";
    // Need to change the eventSender to whatever detects the object in the camera
    public mqttReceiver _eventSender;
    public string topicPublish = "b11/is_in_same_area"; // topic to publish


    // Start is called before the first frame update
    protected override void Start()
    {
        base.Start();
        // Need to change the "mqttReceiver" part as well
        _eventSender = GameObject.FindGameObjectsWithTag(tagOfTheMQTTReceiver)[0].gameObject.GetComponent<mqttReceiver>();
        _eventSender.OnMessageArrived += OnMessageArrivedHandler;
    }

    // Need to change the function input
    // And set messagePublish based on whether the player is inside
    private void OnMessageArrivedHandler(string newMsg)
    {
        string messagePublish = "1";
        UnityEngine.Debug.Log("Event Fired. The message, from Object " + nameController + " is = " + newMsg);
        client.Publish(topicPublish, System.Text.Encoding.UTF8.GetBytes(messagePublish), MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
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