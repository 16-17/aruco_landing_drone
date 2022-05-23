import rospy
from geometry_msgs.msg import Twist
# from Object_Tracking import SampleClass
from cv_bridge import CvBridge, CvBridgeError
import cv2
from sensor_msgs.msg import Image

class drone_working :
    def __init__(self) :
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/iris_fpv_cam/usb_cam/image_raw",Image,self.callback)
        self.image_pub = rospy.Publisher("image_topic_2",Image)


    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e :
            print(e)
    def image_detection(self):
        
def main():
  rospy.init_node("cv_bridge",anonymous=True)
  drone = drone_working()
  try:
    rospy.spin()
    
  except:
    print("error")


  cv2.destroyAllWindows()


main()
