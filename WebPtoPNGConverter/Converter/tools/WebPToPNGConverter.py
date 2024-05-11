import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

/**
 * WebPToPNGConverter tool class to convert .webp files to .png format.
 * This class uses the 'sharp' library to handle the image conversion.
 */
class WebPToPNGConverter {
    inputFilePath: string;
    outputDirectory: string;

    /**
     * Constructor for WebPToPNGConverter.
     * @param inputFilePath - The path to the .webp file to be converted.
     * @param outputDirectory - The directory where the converted .png file will be saved.
     */
    constructor(inputFilePath: string, outputDirectory: string) {
        this.inputFilePath = inputFilePath;
        this.outputDirectory = outputDirectory;
    }

    /**
     * Converts the .webp file to .png format and saves it to the specified directory.
     */
    async convertToPNG(): Promise<void> {
        try {
            const outputFilePath = path.join(this.outputDirectory, path.basename(this.inputFilePath, '.webp') + '.png');
            await sharp(this.inputFilePath)
                .toFormat('png')
                .toFile(outputFilePath);

            console.log(`Conversion successful: ${outputFilePath}`);
        } catch (error) {
            console.error('Error during the conversion process:', error);
        }
    }
}

// Example usage:
// const converter = new WebPToPNGConverter('path/to/input.webp', 'path/to/output');
// converter.convertToPNG();