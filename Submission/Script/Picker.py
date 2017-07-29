import maya.cmds

def resetControls():
    #creates a list of the control shapes
    control_shapes = cmds.ls("ctrl_*", type="nurbsCurve")
    #for each control shape in the list, reset the transformations
    for control_shape in control_shapes:
            # get the parent transform or the nurbs shape, this function returns a list of objects
            parent_objects = cmds.listRelatives(control_shape, parent=True)
            # get the first parent from the list. This is the transform object we are looking for
            control_shape_transform = parent_objects[0]
            #to reset the control shape transform we reset the translation and rotation attributes
            #back to zero and reset the scale attributes to one.
            #we also need check each attribute isn't locked before trying to reset it
            
            #reset translation
            if cmds.getAttr(control_shape_transform+".translateX", lock=True) is False:
                cmds.setAttr(control_shape_transform+".translateX", 0)
            if cmds.getAttr(control_shape_transform+".translateY", lock=True) is False:
                cmds.setAttr(control_shape_transform+".translateY", 0)
            if cmds.getAttr(control_shape_transform+".translateZ", lock=True) is False:
                cmds.setAttr(control_shape_transform+".translateZ", 0)
                
            # reset rotation
            if cmds.getAttr(control_shape_transform+".rotateX", lock=True) is False:
                cmds.setAttr(control_shape_transform+".rotateX", 0)
            if cmds.getAttr(control_shape_transform+".rotateY", lock=True) is False:
                cmds.setAttr(control_shape_transform+".rotateY", 0)
            if cmds.getAttr(control_shape_transform+".rotateZ", lock=True) is False:
                cmds.setAttr(control_shape_transform+".rotateZ", 0)
                
            #reset scale
            if cmds.getAttr(control_shape_transform+".scaleX", lock=True) is False:
                cmds.setAttr(control_shape_transform+".scaleX", 1)
            if cmds.getAttr(control_shape_transform+".scaleY", lock=True) is False:
                cmds.setAttr(control_shape_transform+".scaleY", 1)
            if cmds.getAttr(control_shape_transform+".scaleZ", lock=True) is False:
                cmds.setAttr(control_shape_transform+".scaleZ", 1)

def selectButton(label):
    print label # test
    maya.cmds.select("ctrl_"+label)

#create a window
main_window = maya.cmds.window(title="Model Picker")
#create form layout
model_picker = maya.cmds.formLayout()
#placing an image for the background, this should be found in
#Documents\maya\<maya version>\prefs\icons folder 
backGround = maya.cmds.image(image="Spy.jpg")
#creating the buttons    
r_wrist_button = maya.cmds.button(label="R_Wrist", command="pass")
l_wrist_button = maya.cmds.button(label="L_Wrist", command="pass")
r_ankle_button = maya.cmds.button(label="R_Ankle", command="pass")
l_ankle_button = maya.cmds.button(label="L_Ankle", command="pass")
r_shoulder_button = maya.cmds.button(label="R_Shoulder", command="pass")
l_shoulder_button = maya.cmds.button(label="L_Shoulder", command="pass")
spine_top_button = maya.cmds.button(label="Spine_Top", command="pass")
spine_mid_button = maya.cmds.button(label="Spine_Mid", command="pass")
spine_root_button = maya.cmds.button(label="Spine_Root", command="pass")
root_button = maya.cmds.button(label="Root", command="pass")
master_button = maya.cmds.button(label="Master", command="pass")
reset_button = maya.cmds.button(label="Reset", command="pass")
#Inorder for the selectButton function to receive the label of a specific button
#Ask that specific button what its label is
r_wrist_label = maya.cmds.button(r_wrist_button, query=True, label=True)
l_wrist_label = maya.cmds.button(l_wrist_button, query=True, label=True)
r_ankle_label = maya.cmds.button(r_ankle_button, query=True, label=True)
l_ankle_label = maya.cmds.button(l_ankle_button, query=True, label=True)
r_shoulder_label = maya.cmds.button(r_shoulder_button, query=True, label=True)
l_shoulder_label = maya.cmds.button(l_shoulder_button, query=True, label=True)
spine_top_label = maya.cmds.button(spine_top_button, query=True, label=True)
spine_mid_label = maya.cmds.button(spine_mid_button, query=True, label=True)
spine_root_label = maya.cmds.button(spine_root_button, query=True, label=True)
root_label = maya.cmds.button(root_button, query=True, label=True)
master_label = maya.cmds.button(master_button, query=True, label=True)
#then re-enter edit mode and have the buttons call the new command, sending it the string of the label
#maya.cmds.button(face_button, edit=True, command="faceView")
maya.cmds.button(r_wrist_button, edit=True, command="selectButton('"+r_wrist_label+"')")
maya.cmds.button(l_wrist_button, edit=True, command="selectButton('"+l_wrist_label+"')")
maya.cmds.button(r_ankle_button, edit=True, command="selectButton('"+r_ankle_label+"')")
maya.cmds.button(l_ankle_button, edit=True, command="selectButton('"+l_ankle_label+"')")
maya.cmds.button(r_shoulder_button, edit=True, command="selectButton('"+r_shoulder_label+"')")
maya.cmds.button(l_shoulder_button, edit=True, command="selectButton('"+l_shoulder_label+"')")
maya.cmds.button(spine_top_button, edit=True, command="selectButton('"+spine_top_label+"')")
maya.cmds.button(spine_mid_button, edit=True, command="selectButton('"+spine_mid_label+"')")
maya.cmds.button(spine_root_button, edit=True, command="selectButton('"+spine_root_label+"')")
maya.cmds.button(root_button, edit=True, command="selectButton('"+root_label+"')")
maya.cmds.button(master_button, edit=True, command="selectButton('"+master_label+"')")
maya.cmds.button(reset_button, edit=True, command="resetControls()")
#then amend its position
maya.cmds.setParent("..")
#positioning the controls
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[backGround, "top", 0], [backGround, "left", 0]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[r_wrist_button, "top", 200], [r_wrist_button, "left", 50]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[l_wrist_button, "top", 200], [l_wrist_button, "left", 360]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[r_ankle_button, "top", 450], [r_ankle_button, "left", 100]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[l_ankle_button, "top", 450], [l_ankle_button, "left", 310]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[r_shoulder_button, "top", 60], [r_shoulder_button, "left", 85]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[l_shoulder_button, "top", 60], [l_shoulder_button, "left", 310]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[spine_top_button, "top", 80], [spine_top_button, "left", 200]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[spine_mid_button, "top", 150], [spine_mid_button, "left", 200]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[spine_root_button, "top", 190], [spine_root_button, "left", 200]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[root_button, "top", 220], [root_button, "left", 210]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[master_button, "top", 450], [master_button, "left", 202]])
maya.cmds.formLayout(model_picker, edit=True, attachForm=[[reset_button, "top", 410], [reset_button, "left", 205]])

maya.cmds.showWindow(main_window)

########faceView
#create a window
face_window = maya.cmds.window(title="Face Picker")
#create form layout
face_picker = maya.cmds.formLayout()
#image
face_backGround = maya.cmds.image(image="Face.jpg")
#buttons
jaw_button = maya.cmds.button(label="Jaw", command="pass")
neck_button = maya.cmds.button(label="Neck", command="pass")
head_button = maya.cmds.button(label="Head", command="pass")
eyes_button = maya.cmds.button(label="Eyes", command="pass")
brows_button = maya.cmds.button(label="Brows", command="pass")
#jaw_button = maya.cmds.button(label="Brow", command="pass")
jaw_label = maya.cmds.button(jaw_button, query=True, label=True)
neck_label = maya.cmds.button(neck_button, query=True, label=True)
head_label = maya.cmds.button(head_button, query=True, label=True)
eyes_label = maya.cmds.button(eyes_button, query=True, label=True)
brows_label = maya.cmds.button(brows_button, query=True, label=True)
#jaw_label = maya.cmds.button(jaw_button, query=True, label=True)
maya.cmds.button(jaw_button, edit=True, command="selectButton('"+jaw_label+"')")
maya.cmds.button(neck_button, edit=True, command="selectButton('"+neck_label+"')")
maya.cmds.button(head_button, edit=True, command="selectButton('"+head_label+"')")
maya.cmds.button(eyes_button, edit=True, command="selectButton('"+eyes_label+"')")
maya.cmds.button(brows_button, edit=True, command="selectButton('"+brows_label+"')")

maya.cmds.formLayout(face_picker, edit=True, attachForm=[[face_backGround, "top", 0], [face_backGround, "left", 0]])
maya.cmds.formLayout(face_picker, edit=True, attachForm=[[jaw_button, "top", 230], [jaw_button, "left", 161]])
maya.cmds.formLayout(face_picker, edit=True, attachForm=[[neck_button, "top", 200], [neck_button, "left", 40]])
maya.cmds.formLayout(face_picker, edit=True, attachForm=[[head_button, "top", 200], [head_button, "left", 282]])
maya.cmds.formLayout(face_picker, edit=True, attachForm=[[eyes_button, "top", 100], [eyes_button, "left", 40]])
maya.cmds.formLayout(face_picker, edit=True, attachForm=[[brows_button, "top", 60], [brows_button, "left", 40]])

maya.cmds.showWindow(face_window)