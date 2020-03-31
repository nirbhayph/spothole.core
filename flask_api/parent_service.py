# author: nirbhay pherwani. (https://nirbhay.me, pherwani37@gmail.com, np5318@rit.edu, https://github.com/nirbhayph)
# is the parent service which communicates with the deep learning model
# uses the tensor-flow compressed model created.
# uses the cv2 package for managing the bounding boxes
import cv2
import sys
import utility
import os


# validates single image (accepts image url)
# communicates with the dark-flow
# machine learning model
# to perform the validation
# creates the bounding box and returns the validated image url
def single_image_detection_results(image_url):
    # get local path using image url
    image_path = get_image_local_path(image_url)

    #  add the dark flow deep learning model to the system path
    sys.path.insert(0, utility.DARKFLOW_PATH)

    # import the dark flow net
    from darkflow.net.build import TFNet

    # options for running the test operation
    options = {"model": utility.MODEL_CFG_PATH,
               "pbLoad": utility.PROTOBUF_PATH,
               "metaLoad": utility.META_FILE_PATH,
               "threshold": utility.DEFAULT_THRESHOLD}

    # initialize the net
    tfnet = TFNet(options)

    # read uploaded image
    image_cv = cv2.imread(image_path)

    # store returned dict in result
    result = tfnet.return_predict(image_cv)

    # validation flag to be returned
    validated = False

    if len(result) > 0:
        validated = True

    # iterate over every detection
    for item in result:
        # draw bounding box for current detection
        image_cv = cv2.rectangle(image_cv, (item[utility.LABEL_TOP_LEFT][utility.LABEL_X],
                                            item[utility.LABEL_TOP_LEFT][utility.LABEL_Y]),
                                 (item[utility.LABEL_BOTTOM_RIGHT][utility.LABEL_X],
                                  item[utility.LABEL_BOTTOM_RIGHT][utility.LABEL_Y]),
                                 (0, 255, 0), 4)

        # add text output label
        text_x, text_y = item[utility.LABEL_TOP_LEFT][utility.LABEL_X] - utility.BOX_OFFSET, \
                         item[utility.LABEL_TOP_LEFT][utility.LABEL_Y] - utility.BOX_OFFSET

        image_cv = cv2.putText(image_cv, item[utility.LABEL], (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                               (0, 255, 0), 2,
                               cv2.LINE_AA)

    image_path_slices = image_path.split('/')

    # get image name
    image_name = image_path_slices[-1]

    # remove image name from slices
    image_path_slices.pop()

    # join slices
    output_folder_path = '/'.join(image_path_slices) + '/out/'

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # create output image file path
    image_output_path = output_folder_path + image_name

    # write output image file
    cv2.imwrite(image_output_path, image_cv)

    # output image url to be returned
    output_image_url = get_image_global_path(image_output_path)

    # return urls of boolean associated testing results
    if validated:
        return output_image_url + " : Your image is valid!"
    else:
        return output_image_url + " : Your image is invalid!"


def get_image_local_path(image_url):
    return image_url.replace(utility.DOMAIN_NAME, utility.WEB_DIR_PATH)


def get_image_global_path(image_url):
    return image_url.replace(utility.WEB_DIR_PATH, utility.DOMAIN_NAME)
