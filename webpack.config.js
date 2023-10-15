const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const { SourceMapDevToolPlugin } = require("webpack");
const path = require('path');

module.exports = {
    entry: './static/assets/index.js',  // path to our input file
    output: {
        filename: '[name].bundle.js',  // output bundle file name
        path: path.resolve(__dirname, './static/dist'),  // path to our Django static directory
    },

    module: {
        rules: [
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader'],
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: 'file-loader',
                options: {
                    outputPath: 'static/images/'
                }
            },
            {
                test: /\.(ttf|eot|svg|gif|woff|woff2)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                use: [{
                    loader: 'file-loader',
                }]
            },
        ],
    },
    resolve: {
        extensions: ['', '.js', '.jsx', '.css']
    },
    plugins: [
        new MiniCssExtractPlugin(),
        new SourceMapDevToolPlugin({
            filename: "[file].map"
        })
    ],
    optimization: {
        minimizer: [
            new CssMinimizerPlugin()
        ]
    },
};