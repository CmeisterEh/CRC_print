from CRC_Generator.CRC_Generator import crc_Generator

debugging = 0xFF


class crc_FileWrite:
    def __init__(self, data_length = 8, crc_code = 0x11021, variable_type = 'int',

                       pre_array_syntax = '{',
                      post_array_syntax = '}',
                     after_array_syntax = '',
                     characters_per_line = 70):

        self.formatting = [variable_type, pre_array_syntax, post_array_syntax, after_array_syntax, characters_per_line]
        self.crc_details = [data_length, crc_code]
        self.number_format = 'hex'
        self.Error = 0


    def return_Error(self):
        return self.Error


    def print_to_file(self):



        if debugging == True: print("Just before")
        try:
            file = open("crc_codeword_whole.txt", "w") # Print whole CRC Remainder to file
            if debugging == True: print("File opened")
            crc = crc_Generator(self.crc_details[0], self.crc_details[1])
            if debugging == True: print("Here")


            #preamble
            header_string = "%s crc_codeword = %s" % (self.formatting[0], self.formatting[1])
            if debugging == True: print("header_string: ", header_string)
            file.write(header_string)
            file.write("\n")

            largest_number = 0x00
            for x in range(self.crc_details[0]):
                largest_number = largest_number << 1
                largest_number = largest_number | 0x01
                if debugging == True: print("Largest Number: ", largest_number)

            for i in range ( int((largest_number+1) / 8) ):
                for j in range(8):
                    data = i*8+j
                    crc.generate_Remainder(data = data)
                    Codeword = crc.return_Codeword()
                    crc.check_Remainder(Codeword)
                    Remainder = crc.return_Remainder()
                    Error = crc.return_Error()
                    if (Error == 0):
                        file.write("%+10s " % hex(Remainder))
                        if debugging == True: print("%+10s" % hex(Remainder), " ", end ='')
                    else  :
                        file.write("%+10s" % "Error", end = '')
                        if debugging == True: print("%+10s" % "Error", end = '')
                        self.Error = 1
                if debugging == True: print("")
                file.write("\n")




            file.write("%s%s" % (self.formatting[2], self.formatting[3]) )
            file.write("\n")
            file.close()




        except:
            if debugging == True: print("File Write Failure" )
            self.Error = 1

        try:

            numberof_bytes = self.crc_details[1].bit_length() - 1
            if (numberof_bytes % 8): numberof_bytes = int(numberof_bytes // 8 + 1)
            else                   : numberof_bytes = int(numberof_bytes / 8 )
            file = open("crc_codeword_bytes.txt", "w") # Print whole CRC Remainder to file
            crc = crc_Generator(self.crc_details[0], self.crc_details[1])

            print("Number of bytes: ", numberof_bytes)


            for x in range(numberof_bytes):
                print("X byte", x)
                #preamble
                header_string = "%s crc_codeword_byte%s = %s" % (self.formatting[0], x, self.formatting[1])
                if debugging == True: print("header_string: ", header_string)
                file.write(header_string)
                file.write("\n")

                largest_number = 0x00
                for y in range(self.crc_details[0]):
                    largest_number = largest_number << 1
                    largest_number = largest_number | 0x01
                    if debugging == True: print("Largest Number: ", largest_number)

                for i in range ( int((largest_number+1) / 8) ):
                    for j in range(8):
                        data = i*8+j
                        crc.generate_Remainder(data = data)
                        Codeword = crc.return_Codeword()
                        crc.check_Remainder(Codeword)
                        Remainder = crc.return_Remainder()

                        print("Remainder: ", hex(Remainder), " ", end = '\n')
                        print("X        : ", x)

                        for y in range(x):
                            print("Y: ", y, end = '\n')
                            Remainder = Remainder >> (8)
                            print("Remainder: ", hex(Remainder), end = '\n')
                        Remainder = Remainder & 0xFF

                        print("Remainder: ", hex(Remainder), end = '\n')



                        Error = crc.return_Error()
                        if (Error == 0):
                            file.write("%+4s " % hex(Remainder) )
                            #if debugging == True: print("%+10s" % hex(Remainder), " ", end ='')

                        else  :
                            file.write("%+10s" % "Error", end = '')
                            #if debugging == True: print("%+10s" % "Error", end = '')
                            self.Error = 1
                    #if debugging == True: print("")
                    file.write("\n")

                file.write("\n")




            file.write("%s%s" % (self.formatting[2], self.formatting[3]) )
            file.write("\n")
            file.close()

        except:
            if debugging == True: print("File Write Failure" )
            self.Error = 1










if __name__ == "__main__":

    debugging = True

    #import sys
    #temp = sys.stdout
    #sys.stdout = open('log.txt', 'a')
    #Print('CRC Generation Started')

    from datetime import datetime
    date_time = datetime.now()
    print("Year: %4s, Month: %2s, Day: %2s" % (date_time.year, date_time.month, date_time.day))
    print("Hour: %2s,  Minute: %2s, Sec: %2s" % (date_time.hour, date_time.minute, date_time.second))

    print_to = crc_FileWrite()
    print_to.print_to_file()








