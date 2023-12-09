from network import Website , Link
from download import BinaryData, TextData
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    "website_url",
    help="The url to the website.",
    )
parser.add_argument(
    "download_format",
    help="\"BinaryData\" or \"TextData\" For video, audio, image, pdf use BinaryData"
    )
parser.add_argument(
    "output_folder",
    help="Example: ./video/")
parser.add_argument(
    "element",
    help="Search for certain element"
)
parser.add_argument(
    "attribute",
    help="Search for certain attribute in the element",
    nargs="?",
    default=None
)
# the arguments given
args = parser.parse_args()

if __name__=="__main__":
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    website = Website(args.website_url)
    if args.download_format == "BinaryData":
        image_title = website.find_contents_with_element(args.element, "alt")
        image_links = website.find_contents_with_element(args.element, args.attribute)
        for i, link in enumerate(image_links):
            if "https" in link:
                content = Link(link).get_response_content()
                BinaryData(content, f"{image_title[i]}.jpg").download(args.output_folder)
    else:
        element_content = website.find_contents_with_element(args.element, args.attribute)
        for i, content in enumerate(element_content):
            TextData(content, f"text{i}.txt").download(args.output_folder)