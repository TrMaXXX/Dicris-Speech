from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from time import sleep


class Calc_PRODUCT(BasePiece):

	def piece_function(self, input_data: InputModel):

		self.logger.info(f"Make product of {input_data.a_num} {input_data.b_num}")
		ab_product=input_data.a_num*input_data.b_num

		message = f"The product of {input_data.a_num} and {input_data.a_num} is {ab_product}"
		self.logger.info(message)
		# Return output
		return OutputModel(
			message=message,
		)
